#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail
set -o xtrace

wget -O presentation.md https://demo.hedgedoc.org/p3JvovxJRcift27qD9etag/download
pandoc -f markdown -t html presentation.md -o presentation.html --template=template.html

