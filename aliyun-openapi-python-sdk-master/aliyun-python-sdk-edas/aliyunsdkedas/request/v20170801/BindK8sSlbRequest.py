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

from aliyunsdkcore.request import RoaRequest
class BindK8sSlbRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'BindK8sSlb')
		self.set_uri_pattern('/pop/v5/k8s/acs/k8s_slb_binding')
		self.set_method('POST')

	def get_SlbId(self):
		return self.get_query_params().get('SlbId')

	def set_SlbId(self,SlbId):
		self.add_query_param('SlbId',SlbId)

	def get_SlbProtocol(self):
		return self.get_query_params().get('SlbProtocol')

	def set_SlbProtocol(self,SlbProtocol):
		self.add_query_param('SlbProtocol',SlbProtocol)

	def get_Port(self):
		return self.get_query_params().get('Port')

	def set_Port(self,Port):
		self.add_query_param('Port',Port)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_TargetPort(self):
		return self.get_query_params().get('TargetPort')

	def set_TargetPort(self,TargetPort):
		self.add_query_param('TargetPort',TargetPort)