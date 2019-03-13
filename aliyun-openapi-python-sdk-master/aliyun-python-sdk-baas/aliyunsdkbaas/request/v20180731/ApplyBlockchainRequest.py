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
class ApplyBlockchainRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Baas', '2018-07-31', 'ApplyBlockchain')

	def get_Blockchain(self):
		return self.get_body_params().get('Blockchain')

	def set_Blockchain(self,Blockchain):
		self.add_body_params('Blockchain', Blockchain)

	def get_UploadReq(self):
		return self.get_body_params().get('UploadReq')

	def set_UploadReq(self,UploadReq):
		self.add_body_params('UploadReq', UploadReq)