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
class ListInvocationResultsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'EHPC', '2018-04-12', 'ListInvocationResults','ehs')

	def get_Instances(self):
		return self.get_query_params().get('Instances')

	def set_Instances(self,Instances):
		for i in range(len(Instances)):	
			if Instances[i].get('Id') is not None:
				self.add_query_param('Instance.' + str(i + 1) + '.Id' , Instances[i].get('Id'))


	def get_InvokeRecordStatus(self):
		return self.get_query_params().get('InvokeRecordStatus')

	def set_InvokeRecordStatus(self,InvokeRecordStatus):
		self.add_query_param('InvokeRecordStatus',InvokeRecordStatus)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_CommandId(self):
		return self.get_query_params().get('CommandId')

	def set_CommandId(self,CommandId):
		self.add_query_param('CommandId',CommandId)

	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)