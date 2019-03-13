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
class DescribeAlarmsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cms', '2018-03-08', 'DescribeAlarms','cms')

	def get_EnableState(self):
		return self.get_query_params().get('EnableState')

	def set_EnableState(self,EnableState):
		self.add_query_param('EnableState',EnableState)

	def get_Names(self):
		return self.get_query_params().get('Names')

	def set_Names(self,Names):
		self.add_query_param('Names',Names)

	def get_DisplayName(self):
		return self.get_query_params().get('DisplayName')

	def set_DisplayName(self,DisplayName):
		self.add_query_param('DisplayName',DisplayName)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_Namespace(self):
		return self.get_query_params().get('Namespace')

	def set_Namespace(self,Namespace):
		self.add_query_param('Namespace',Namespace)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_AlertState(self):
		return self.get_query_params().get('AlertState')

	def set_AlertState(self,AlertState):
		self.add_query_param('AlertState',AlertState)

	def get_NameKeyword(self):
		return self.get_query_params().get('NameKeyword')

	def set_NameKeyword(self,NameKeyword):
		self.add_query_param('NameKeyword',NameKeyword)

	def get_GroupBy(self):
		return self.get_query_params().get('GroupBy')

	def set_GroupBy(self,GroupBy):
		self.add_query_param('GroupBy',GroupBy)

	def get_Page(self):
		return self.get_query_params().get('Page')

	def set_Page(self,Page):
		self.add_query_param('Page',Page)

	def get_MetricName(self):
		return self.get_query_params().get('MetricName')

	def set_MetricName(self,MetricName):
		self.add_query_param('MetricName',MetricName)