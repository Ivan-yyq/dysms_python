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
class CreateJobFileRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EHPC', '2018-04-12', 'CreateJobFile','ehs')

	def get_TargetFile(self):
		return self.get_query_params().get('TargetFile')

	def set_TargetFile(self,TargetFile):
		self.add_query_param('TargetFile',TargetFile)

	def get_RunasUserPassword(self):
		return self.get_query_params().get('RunasUserPassword')

	def set_RunasUserPassword(self,RunasUserPassword):
		self.add_query_param('RunasUserPassword',RunasUserPassword)

	def get_RunasUser(self):
		return self.get_query_params().get('RunasUser')

	def set_RunasUser(self,RunasUser):
		self.add_query_param('RunasUser',RunasUser)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_Content(self):
		return self.get_query_params().get('Content')

	def set_Content(self,Content):
		self.add_query_param('Content',Content)