#!/bin/bash
# Script that takes in a URL, sends a request to that URL, and displays the size of the body of the reponse
curl -s -w '%{size_download}\n' "$1"
