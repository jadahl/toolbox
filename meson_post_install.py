#!/usr/bin/env python3
#
# Copyright © 2021 – 2022 Red Hat Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import subprocess
import sys

destdir = os.environ.get('DESTDIR', '')

if not destdir and not os.path.exists('/run/.containerenv'):
    print('Calling systemd-tmpfiles --create ...')

    try:
        subprocess.run(['systemd-tmpfiles', '--create'], check=True)
    except subprocess.CalledProcessError as e:
        print('Returned non-zero exit status', e.returncode)
        sys.exit(e.returncode)

sys.exit(0)
