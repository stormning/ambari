#!/usr/bin/env python
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

from resource_management.libraries.script.script import Script

def get_component_repository_version(service_name, component_name = None):
  """
  Gets the version associated with the specified component from the structure in the command.
  Every command should contain a mapping of service/component to the desired repository it's set
  to.

  :service_name: the name of the service
  :component_name: the name of the component
  """
  versions = _get_component_repositories()
  if versions is None:
    return None

  if service_name not in versions:
    return None

  component_versions = versions[service_name]
  if len(component_versions) == 0:
    return None

  if component_name is None:
    for component in component_versions:
      return component_versions[component]

  if not component_name in component_versions:
    return None

  return component_versions[component_name]


def _get_component_repositories():
  """
  Gets an initialized dictionary from the value in componentVersionMap. This structure is
  sent on every command by Ambari and should contain each service & component's desired repository.
  :return:
  """
  config = Script.get_config()
  if "componentVersionMap" not in config or config["componentVersionMap"] is "":
    return None

  return config["componentVersionMap"]