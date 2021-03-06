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
class InsertOrUpdateRegionRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'InsertOrUpdateRegion')
		self.set_uri_pattern('/pop/v5/user_region_def')
		self.set_method('POST')

	def get_HybridCloudEnable(self):
		return self.get_query_params().get('HybridCloudEnable')

	def set_HybridCloudEnable(self,HybridCloudEnable):
		self.add_query_param('HybridCloudEnable',HybridCloudEnable)

	def get_VpcId(self):
		return self.get_query_params().get('VpcId')

	def set_VpcId(self,VpcId):
		self.add_query_param('VpcId',VpcId)

	def get_RegionTag(self):
		return self.get_query_params().get('RegionTag')

	def set_RegionTag(self,RegionTag):
		self.add_query_param('RegionTag',RegionTag)

	def get_RegionName(self):
		return self.get_query_params().get('RegionName')

	def set_RegionName(self,RegionName):
		self.add_query_param('RegionName',RegionName)

	def get_Description(self):
		return self.get_query_params().get('Description')

	def set_Description(self,Description):
		self.add_query_param('Description',Description)

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)