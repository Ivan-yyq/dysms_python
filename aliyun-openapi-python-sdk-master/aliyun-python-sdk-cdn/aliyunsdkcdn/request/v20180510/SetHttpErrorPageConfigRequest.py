# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class SetHttpErrorPageConfigRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cdn', '2018-05-10', 'SetHttpErrorPageConfig')

	def get_PageUrl(self):
		return self.get_query_params().get('PageUrl')

	def set_PageUrl(self,PageUrl):
		self.add_query_param('PageUrl',PageUrl)

	def get_ErrorCode(self):
		return self.get_query_params().get('ErrorCode')

	def set_ErrorCode(self,ErrorCode):
		self.add_query_param('ErrorCode',ErrorCode)

	def get_DomainName(self):
		return self.get_query_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_query_param('DomainName',DomainName)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_ConfigId(self):
		return self.get_query_params().get('ConfigId')

	def set_ConfigId(self,ConfigId):
		self.add_query_param('ConfigId',ConfigId)