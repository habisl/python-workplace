#!/usr/bin/env python3
"""Python script to sort out files for uploading in the artifactory.
The script returns the list of files in JSON format to parse
in the Jenkinsfile.
Example usage:
To get the files changed in the last commit:
    $ python3 scripts/update_changes.py latest_changes
To get all active channel files:
    $ python3 scripts/update_changes.py all_channels
"""
import argparse
import configparser
import glob
import json
import os
import urllib.request
EXTENSIONS = ['.spc', '.cfg', '.json']
def get_active_channels():
    """Sort out the channels which currently have active status"""
    active_channels = []
    for file in glob.glob('channels/*/*'):
        if file.endswith('.cfg'):
            config = configparser.ConfigParser()
            active_channels.extend(
                file
                for file in config.read(file)
                if config.has_option("channel", "www-enabled")
                and config['channel']['www-enabled'] == 'true'
            )
    return active_channels
def channel_list():
    """Create the channel list based on channel's active status"""
    channels = []
    paths = get_active_channels()
    for path in paths:
        split_lines = path.split("/")
        channel_name = split_lines[1] # Channel name is in the second position /channels/arm-11/..
        channels.append(channel_name)
    return channels
def find_commit_changes():
    """Get the files that got changed in the last commit"""
    build_url = os.environ['BUILD_URL']
    api = f'{build_url}api/json/'
    f = urllib.request.urlopen(api)
    build = json.loads(f.read())
    try:
        change_set = build['changeSets']
        items = change_set[0]['items']
        changed_files = []
        for item in items:
            changed_files += item['affectedPaths']
        return changed_files
    except IndexError:
        return None
def json_fileinfo(paths):
    """Return the file info in json format"""
    ch = channel_list()
    file_info = {}
    files = []
    for path in paths:
        split_lines = path.split("/")
        channel_name = split_lines[1]
        file_name = split_lines[2]
        file_extension = os.path.splitext(file_name)[1]
        if channel_name in ch and file_extension in EXTENSIONS:
            file_info = {
                "name": file_name,
                "channel": channel_name,
                "path": path
            }
        files.append(file_info)
    return json.dumps(files, indent=4)
def get_commit_changes():
    """Returns the json format of the modified files"""
    changed = find_commit_changes()
    m = ("No changes")
    if changed is None:
        return m
    paths = [i for i in changed if i.startswith('channels/')]
    if not paths:
        return m
    return json_fileinfo(paths)
def find_all_channel_files():
    """List all files for the active channels in the channel directory"""
    ch = channel_list()
    all_channel_files= []
    for file in glob.glob('channels/*/*'):
        if file.endswith(tuple(EXTENSIONS)):
            all_channel_files.append(file)
            for element in all_channel_files:
                split_lines = element.split("/")
                channel_name = split_lines[1]
                if channel_name not in ch:
                    all_channel_files.remove(element)
    return json_fileinfo(all_channel_files)
def _print_commit_changes():
    output= get_commit_changes()
    print(output)
def _print_all_channel_files():
    output= find_all_channel_files()
    print(output)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("function",
                        nargs="?",
                        choices=['latest_changes', 'all_channels']
                        )
    args, sub_args = parser.parse_known_args()
    if args.function == "latest_changes":
        _print_commit_changes()
    elif args.function == "all_channels":
        _print_all_channel_files()
if __name__ == "__main__":
        main()
