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
class CreateConsortiumRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Baas', '2018-07-31', 'CreateConsortium')

	def get_OrderersCount(self):
		return self.get_body_params().get('OrderersCount')

	def set_OrderersCount(self,OrderersCount):
		self.add_body_params('OrderersCount', OrderersCount)

	def get_Domain(self):
		return self.get_body_params().get('Domain')

	def set_Domain(self,Domain):
		self.add_body_params('Domain', Domain)

	def get_SpecName(self):
		return self.get_body_params().get('SpecName')

	def set_SpecName(self,SpecName):
		self.add_body_params('SpecName', SpecName)

	def get_Organizations(self):
		return self.get_body_params().get('Organizations')

	def set_Organizations(self,Organizations):
		for i in range(len(Organizations)):	
			if Organizations[i].get('Id') is not None:
				self.add_body_params('Organization.' + str(i + 1) + '.Id' , Organizations[i].get('Id'))


	def get_Name(self):
		return self.get_body_params().get('Name')

	def set_Name(self,Name):
		self.add_body_params('Name', Name)

	def get_OrdererType(self):
		return self.get_body_params().get('OrdererType')

	def set_OrdererType(self,OrdererType):
		self.add_body_params('OrdererType', OrdererType)

	def get_ZoneId(self):
		return self.get_body_params().get('ZoneId')

	def set_ZoneId(self,ZoneId):
		self.add_body_params('ZoneId', ZoneId)

	def get_Description(self):
		return self.get_body_params().get('Description')

	def set_Description(self,Description):
		self.add_body_params('Description', Description)

	def get_Location(self):
		return self.get_body_params().get('Location')

	def set_Location(self,Location):
		self.add_body_params('Location', Location)

	def get_PeersCount(self):
		return self.get_body_params().get('PeersCount')

	def set_PeersCount(self,PeersCount):
		self.add_body_params('PeersCount', PeersCount)

	def get_ChannelPolicy(self):
		return self.get_body_params().get('ChannelPolicy')

	def set_ChannelPolicy(self,ChannelPolicy):
		self.add_body_params('ChannelPolicy', ChannelPolicy)