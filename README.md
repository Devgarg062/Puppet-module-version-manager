# Puppet Module Version Manager

## Overview
This project implements a CLI-based Puppet Module Version Manager that allows users to manage different versions of Puppet modules stored locally.

## Features
- List available module versions
- Install a specific module version
- Switch between module versions
- Remove installed modules
- Track installed modules using a registry file

## Project Structure

modules_repo/
  Contains all module versions

installed_modules/
  Contains currently installed modules

versions.json
  Tracks installed module versions

manager.py
  CLI tool for module management

## Commands

List versions
python manager.py list apache

Install version
python manager.py install apache 1.0.0

Check installed modules
python manager.py current

Remove module
python manager.py remove apache

## Technologies Used
- Python
- CLI automation
- Local file system management