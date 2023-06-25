# SPDX-FileCopyrightText: 2022 Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
# ########################## DO NOT EDIT FILE ############################
# All code in this module is auto generated by Quicktype
# See https://github.com/quicktype/quicktype for general documentation.
# 1 - Make a "name_of_your_file.graphql" file.
# 2 - Contents of file must be the query, you wish to generate models from, uncommented.
# 3 - Stand in directory of your "name_of_your_file.graphql" file and run the
# following command with the path to the query to generate from:
# $ quicktype --src-lang graphql --lang py --python-version 3.7 \
#    --graphql-introspect https://moradev.magentahosted.dk/graphql/v7 \
#    get_job_functions.graphql --just-types
#
# 4 - The model will be shown in terminal. Copy and paste the output in your file.
# query GetJobFunctions {
#   engagements {
#     objects {
#       current {
#         extension_1
#         extension_10
#         extension_2
#         extension_3
#         extension_4
#         extension_5
#         extension_6
#         extension_7
#         extension_8
#         extension_9
#         fraction
#         job_function {
#           full_name
#           user_key
#           uuid
#         }
#       }
#       uuid
#     }
#   }
# }
from dataclasses import dataclass


@dataclass
class Class:
    full_name: str
    user_key: str | None = None
    uuid: str | None = None


@dataclass
class Engagement:
    job_function: Class
    extension_1: str | None = None
    extension_10: str | None = None
    extension_2: str | None = None
    extension_3: str | None = None
    extension_4: str | None = None
    extension_5: str | None = None
    extension_6: str | None = None
    extension_7: str | None = None
    extension_8: str | None = None
    extension_9: str | None = None
    fraction: int | None = None


@dataclass
class EngagementResponse:
    uuid: str
    current: Engagement | None = None


@dataclass
class EngagementResponsePaged:
    objects: list[EngagementResponse]


@dataclass
class Data:
    engagements: EngagementResponsePaged


@dataclass
class Error:
    message: str


@dataclass
class GetJobFunctions:
    data: Data | None = None
    errors: list[Error] | None = None
