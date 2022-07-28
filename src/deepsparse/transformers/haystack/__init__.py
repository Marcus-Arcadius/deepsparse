# Copyright (c) 2021 - present / Neuralmagic, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Helpers for running haystack pipelines and nodes with DeepSparse and integrating
deepset-ai/haystack
"""

# flake8: noqa
# isort: skip_file

import os as os
from deepsparse.auto_install import auto_pip_install, Dependency

_HAYSTACK_REQS_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "haystack_reqs.txt",
    )
)

auto_pip_install(
    __qualname__,
    Dependency(
        "farm-haystack[all]",
        version="==1.4.0",
        import_name="haystack",
        requirements=[f"-r {_HAYSTACK_REQS_PATH}"],
    ),
)


from .nodes import *
from .pipeline import *
from .helpers import *

__all__ = nodes.__all__ + pipeline.__all__ + helpers.__all__