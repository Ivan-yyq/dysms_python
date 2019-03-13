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
class InstantiateChaincodeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Baas', '2018-07-31', 'InstantiateChaincode')

	def get_OrganizationId(self):
		return self.get_body_params().get('OrganizationId')

	def set_OrganizationId(self,OrganizationId):
		self.add_body_params('OrganizationId', OrganizationId)

	def get_ChaincodeId(self):
		return self.get_body_params().get('ChaincodeId')

	def set_ChaincodeId(self,ChaincodeId):
		self.add_body_params('ChaincodeId', ChaincodeId)

	def get_EndorsePolicy(self):
		return self.get_body_params().get('EndorsePolicy')

	def set_EndorsePolicy(self,EndorsePolicy):
		self.add_body_params('EndorsePolicy', EndorsePolicy)

	def get_Location(self):
		return self.get_body_params().get('Location')

	def set_Location(self,Location):
		self.add_body_params('Location', Location)