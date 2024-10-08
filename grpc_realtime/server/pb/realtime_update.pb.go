// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.34.2
// 	protoc        v5.27.2
// source: realtime_update.proto

package pb

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type TargetData int32

const (
	TargetData_TARGETDATA_UNKNOWN TargetData = 0
	TargetData_SPOT               TargetData = 1
	TargetData_VOL                TargetData = 2
)

// Enum value maps for TargetData.
var (
	TargetData_name = map[int32]string{
		0: "TARGETDATA_UNKNOWN",
		1: "SPOT",
		2: "VOL",
	}
	TargetData_value = map[string]int32{
		"TARGETDATA_UNKNOWN": 0,
		"SPOT":               1,
		"VOL":                2,
	}
)

func (x TargetData) Enum() *TargetData {
	p := new(TargetData)
	*p = x
	return p
}

func (x TargetData) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (TargetData) Descriptor() protoreflect.EnumDescriptor {
	return file_realtime_update_proto_enumTypes[0].Descriptor()
}

func (TargetData) Type() protoreflect.EnumType {
	return &file_realtime_update_proto_enumTypes[0]
}

func (x TargetData) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use TargetData.Descriptor instead.
func (TargetData) EnumDescriptor() ([]byte, []int) {
	return file_realtime_update_proto_rawDescGZIP(), []int{0}
}

type RealtimeMarketRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Ip               string       `protobuf:"bytes,1,opt,name=ip,proto3" json:"ip,omitempty"`
	UpdateInterval   int32        `protobuf:"varint,2,opt,name=update_interval,json=updateInterval,proto3" json:"update_interval,omitempty"`
	TargetTickerList []string     `protobuf:"bytes,3,rep,name=target_ticker_list,json=targetTickerList,proto3" json:"target_ticker_list,omitempty"`
	TargetDataList   []TargetData `protobuf:"varint,4,rep,packed,name=target_data_list,json=targetDataList,proto3,enum=TargetData" json:"target_data_list,omitempty"`
}

func (x *RealtimeMarketRequest) Reset() {
	*x = RealtimeMarketRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_realtime_update_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *RealtimeMarketRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*RealtimeMarketRequest) ProtoMessage() {}

func (x *RealtimeMarketRequest) ProtoReflect() protoreflect.Message {
	mi := &file_realtime_update_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use RealtimeMarketRequest.ProtoReflect.Descriptor instead.
func (*RealtimeMarketRequest) Descriptor() ([]byte, []int) {
	return file_realtime_update_proto_rawDescGZIP(), []int{0}
}

func (x *RealtimeMarketRequest) GetIp() string {
	if x != nil {
		return x.Ip
	}
	return ""
}

func (x *RealtimeMarketRequest) GetUpdateInterval() int32 {
	if x != nil {
		return x.UpdateInterval
	}
	return 0
}

func (x *RealtimeMarketRequest) GetTargetTickerList() []string {
	if x != nil {
		return x.TargetTickerList
	}
	return nil
}

func (x *RealtimeMarketRequest) GetTargetDataList() []TargetData {
	if x != nil {
		return x.TargetDataList
	}
	return nil
}

type RealtimeMarketResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	EquityDataList []*EquityData `protobuf:"bytes,1,rep,name=equity_data_list,json=equityDataList,proto3" json:"equity_data_list,omitempty"`
}

func (x *RealtimeMarketResponse) Reset() {
	*x = RealtimeMarketResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_realtime_update_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *RealtimeMarketResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*RealtimeMarketResponse) ProtoMessage() {}

func (x *RealtimeMarketResponse) ProtoReflect() protoreflect.Message {
	mi := &file_realtime_update_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use RealtimeMarketResponse.ProtoReflect.Descriptor instead.
func (*RealtimeMarketResponse) Descriptor() ([]byte, []int) {
	return file_realtime_update_proto_rawDescGZIP(), []int{1}
}

func (x *RealtimeMarketResponse) GetEquityDataList() []*EquityData {
	if x != nil {
		return x.EquityDataList
	}
	return nil
}

type EquityData struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Ticker     string             `protobuf:"bytes,1,opt,name=ticker,proto3" json:"ticker,omitempty"`
	SpotData   *SpotData          `protobuf:"bytes,2,opt,name=spot_data,json=spotData,proto3" json:"spot_data,omitempty"`
	SigmaData  map[string]float64 `protobuf:"bytes,3,rep,name=sigma_data,json=sigmaData,proto3" json:"sigma_data,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"fixed64,2,opt,name=value,proto3"`
	AlphaData  map[string]float64 `protobuf:"bytes,4,rep,name=alpha_data,json=alphaData,proto3" json:"alpha_data,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"fixed64,2,opt,name=value,proto3"`
	AlphaRData map[string]float64 `protobuf:"bytes,5,rep,name=alphaR_data,json=alphaRData,proto3" json:"alphaR_data,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"fixed64,2,opt,name=value,proto3"`
	BetaData   map[string]float64 `protobuf:"bytes,6,rep,name=beta_data,json=betaData,proto3" json:"beta_data,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"fixed64,2,opt,name=value,proto3"`
	RhoData    map[string]float64 `protobuf:"bytes,7,rep,name=rho_data,json=rhoData,proto3" json:"rho_data,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"fixed64,2,opt,name=value,proto3"`
}

func (x *EquityData) Reset() {
	*x = EquityData{}
	if protoimpl.UnsafeEnabled {
		mi := &file_realtime_update_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *EquityData) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*EquityData) ProtoMessage() {}

func (x *EquityData) ProtoReflect() protoreflect.Message {
	mi := &file_realtime_update_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use EquityData.ProtoReflect.Descriptor instead.
func (*EquityData) Descriptor() ([]byte, []int) {
	return file_realtime_update_proto_rawDescGZIP(), []int{2}
}

func (x *EquityData) GetTicker() string {
	if x != nil {
		return x.Ticker
	}
	return ""
}

func (x *EquityData) GetSpotData() *SpotData {
	if x != nil {
		return x.SpotData
	}
	return nil
}

func (x *EquityData) GetSigmaData() map[string]float64 {
	if x != nil {
		return x.SigmaData
	}
	return nil
}

func (x *EquityData) GetAlphaData() map[string]float64 {
	if x != nil {
		return x.AlphaData
	}
	return nil
}

func (x *EquityData) GetAlphaRData() map[string]float64 {
	if x != nil {
		return x.AlphaRData
	}
	return nil
}

func (x *EquityData) GetBetaData() map[string]float64 {
	if x != nil {
		return x.BetaData
	}
	return nil
}

func (x *EquityData) GetRhoData() map[string]float64 {
	if x != nil {
		return x.RhoData
	}
	return nil
}

type SpotData struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Open float64 `protobuf:"fixed64,1,opt,name=open,proto3" json:"open,omitempty"`
	Low  float64 `protobuf:"fixed64,2,opt,name=low,proto3" json:"low,omitempty"`
	High float64 `protobuf:"fixed64,3,opt,name=high,proto3" json:"high,omitempty"`
	Spot float64 `protobuf:"fixed64,4,opt,name=spot,proto3" json:"spot,omitempty"`
}

func (x *SpotData) Reset() {
	*x = SpotData{}
	if protoimpl.UnsafeEnabled {
		mi := &file_realtime_update_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SpotData) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SpotData) ProtoMessage() {}

func (x *SpotData) ProtoReflect() protoreflect.Message {
	mi := &file_realtime_update_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SpotData.ProtoReflect.Descriptor instead.
func (*SpotData) Descriptor() ([]byte, []int) {
	return file_realtime_update_proto_rawDescGZIP(), []int{3}
}

func (x *SpotData) GetOpen() float64 {
	if x != nil {
		return x.Open
	}
	return 0
}

func (x *SpotData) GetLow() float64 {
	if x != nil {
		return x.Low
	}
	return 0
}

func (x *SpotData) GetHigh() float64 {
	if x != nil {
		return x.High
	}
	return 0
}

func (x *SpotData) GetSpot() float64 {
	if x != nil {
		return x.Spot
	}
	return 0
}

var File_realtime_update_proto protoreflect.FileDescriptor

var file_realtime_update_proto_rawDesc = []byte{
	0x0a, 0x15, 0x72, 0x65, 0x61, 0x6c, 0x74, 0x69, 0x6d, 0x65, 0x5f, 0x75, 0x70, 0x64, 0x61, 0x74,
	0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0xb5, 0x01, 0x0a, 0x15, 0x52, 0x65, 0x61, 0x6c,
	0x74, 0x69, 0x6d, 0x65, 0x4d, 0x61, 0x72, 0x6b, 0x65, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73,
	0x74, 0x12, 0x0e, 0x0a, 0x02, 0x69, 0x70, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x02, 0x69,
	0x70, 0x12, 0x27, 0x0a, 0x0f, 0x75, 0x70, 0x64, 0x61, 0x74, 0x65, 0x5f, 0x69, 0x6e, 0x74, 0x65,
	0x72, 0x76, 0x61, 0x6c, 0x18, 0x02, 0x20, 0x01, 0x28, 0x05, 0x52, 0x0e, 0x75, 0x70, 0x64, 0x61,
	0x74, 0x65, 0x49, 0x6e, 0x74, 0x65, 0x72, 0x76, 0x61, 0x6c, 0x12, 0x2c, 0x0a, 0x12, 0x74, 0x61,
	0x72, 0x67, 0x65, 0x74, 0x5f, 0x74, 0x69, 0x63, 0x6b, 0x65, 0x72, 0x5f, 0x6c, 0x69, 0x73, 0x74,
	0x18, 0x03, 0x20, 0x03, 0x28, 0x09, 0x52, 0x10, 0x74, 0x61, 0x72, 0x67, 0x65, 0x74, 0x54, 0x69,
	0x63, 0x6b, 0x65, 0x72, 0x4c, 0x69, 0x73, 0x74, 0x12, 0x35, 0x0a, 0x10, 0x74, 0x61, 0x72, 0x67,
	0x65, 0x74, 0x5f, 0x64, 0x61, 0x74, 0x61, 0x5f, 0x6c, 0x69, 0x73, 0x74, 0x18, 0x04, 0x20, 0x03,
	0x28, 0x0e, 0x32, 0x0b, 0x2e, 0x54, 0x61, 0x72, 0x67, 0x65, 0x74, 0x44, 0x61, 0x74, 0x61, 0x52,
	0x0e, 0x74, 0x61, 0x72, 0x67, 0x65, 0x74, 0x44, 0x61, 0x74, 0x61, 0x4c, 0x69, 0x73, 0x74, 0x22,
	0x4f, 0x0a, 0x16, 0x52, 0x65, 0x61, 0x6c, 0x74, 0x69, 0x6d, 0x65, 0x4d, 0x61, 0x72, 0x6b, 0x65,
	0x74, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x35, 0x0a, 0x10, 0x65, 0x71, 0x75,
	0x69, 0x74, 0x79, 0x5f, 0x64, 0x61, 0x74, 0x61, 0x5f, 0x6c, 0x69, 0x73, 0x74, 0x18, 0x01, 0x20,
	0x03, 0x28, 0x0b, 0x32, 0x0b, 0x2e, 0x45, 0x71, 0x75, 0x69, 0x74, 0x79, 0x44, 0x61, 0x74, 0x61,
	0x52, 0x0e, 0x65, 0x71, 0x75, 0x69, 0x74, 0x79, 0x44, 0x61, 0x74, 0x61, 0x4c, 0x69, 0x73, 0x74,
	0x22, 0xa1, 0x05, 0x0a, 0x0a, 0x45, 0x71, 0x75, 0x69, 0x74, 0x79, 0x44, 0x61, 0x74, 0x61, 0x12,
	0x16, 0x0a, 0x06, 0x74, 0x69, 0x63, 0x6b, 0x65, 0x72, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x06, 0x74, 0x69, 0x63, 0x6b, 0x65, 0x72, 0x12, 0x26, 0x0a, 0x09, 0x73, 0x70, 0x6f, 0x74, 0x5f,
	0x64, 0x61, 0x74, 0x61, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x09, 0x2e, 0x53, 0x70, 0x6f,
	0x74, 0x44, 0x61, 0x74, 0x61, 0x52, 0x08, 0x73, 0x70, 0x6f, 0x74, 0x44, 0x61, 0x74, 0x61, 0x12,
	0x39, 0x0a, 0x0a, 0x73, 0x69, 0x67, 0x6d, 0x61, 0x5f, 0x64, 0x61, 0x74, 0x61, 0x18, 0x03, 0x20,
	0x03, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x45, 0x71, 0x75, 0x69, 0x74, 0x79, 0x44, 0x61, 0x74, 0x61,
	0x2e, 0x53, 0x69, 0x67, 0x6d, 0x61, 0x44, 0x61, 0x74, 0x61, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x52,
	0x09, 0x73, 0x69, 0x67, 0x6d, 0x61, 0x44, 0x61, 0x74, 0x61, 0x12, 0x39, 0x0a, 0x0a, 0x61, 0x6c,
	0x70, 0x68, 0x61, 0x5f, 0x64, 0x61, 0x74, 0x61, 0x18, 0x04, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x1a,
	0x2e, 0x45, 0x71, 0x75, 0x69, 0x74, 0x79, 0x44, 0x61, 0x74, 0x61, 0x2e, 0x41, 0x6c, 0x70, 0x68,
	0x61, 0x44, 0x61, 0x74, 0x61, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x52, 0x09, 0x61, 0x6c, 0x70, 0x68,
	0x61, 0x44, 0x61, 0x74, 0x61, 0x12, 0x3c, 0x0a, 0x0b, 0x61, 0x6c, 0x70, 0x68, 0x61, 0x52, 0x5f,
	0x64, 0x61, 0x74, 0x61, 0x18, 0x05, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x1b, 0x2e, 0x45, 0x71, 0x75,
	0x69, 0x74, 0x79, 0x44, 0x61, 0x74, 0x61, 0x2e, 0x41, 0x6c, 0x70, 0x68, 0x61, 0x52, 0x44, 0x61,
	0x74, 0x61, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x52, 0x0a, 0x61, 0x6c, 0x70, 0x68, 0x61, 0x52, 0x44,
	0x61, 0x74, 0x61, 0x12, 0x36, 0x0a, 0x09, 0x62, 0x65, 0x74, 0x61, 0x5f, 0x64, 0x61, 0x74, 0x61,
	0x18, 0x06, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x19, 0x2e, 0x45, 0x71, 0x75, 0x69, 0x74, 0x79, 0x44,
	0x61, 0x74, 0x61, 0x2e, 0x42, 0x65, 0x74, 0x61, 0x44, 0x61, 0x74, 0x61, 0x45, 0x6e, 0x74, 0x72,
	0x79, 0x52, 0x08, 0x62, 0x65, 0x74, 0x61, 0x44, 0x61, 0x74, 0x61, 0x12, 0x33, 0x0a, 0x08, 0x72,
	0x68, 0x6f, 0x5f, 0x64, 0x61, 0x74, 0x61, 0x18, 0x07, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x18, 0x2e,
	0x45, 0x71, 0x75, 0x69, 0x74, 0x79, 0x44, 0x61, 0x74, 0x61, 0x2e, 0x52, 0x68, 0x6f, 0x44, 0x61,
	0x74, 0x61, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x52, 0x07, 0x72, 0x68, 0x6f, 0x44, 0x61, 0x74, 0x61,
	0x1a, 0x3c, 0x0a, 0x0e, 0x53, 0x69, 0x67, 0x6d, 0x61, 0x44, 0x61, 0x74, 0x61, 0x45, 0x6e, 0x74,
	0x72, 0x79, 0x12, 0x10, 0x0a, 0x03, 0x6b, 0x65, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x03, 0x6b, 0x65, 0x79, 0x12, 0x14, 0x0a, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x18, 0x02, 0x20,
	0x01, 0x28, 0x01, 0x52, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x3a, 0x02, 0x38, 0x01, 0x1a, 0x3c,
	0x0a, 0x0e, 0x41, 0x6c, 0x70, 0x68, 0x61, 0x44, 0x61, 0x74, 0x61, 0x45, 0x6e, 0x74, 0x72, 0x79,
	0x12, 0x10, 0x0a, 0x03, 0x6b, 0x65, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x6b,
	0x65, 0x79, 0x12, 0x14, 0x0a, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28,
	0x01, 0x52, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x3a, 0x02, 0x38, 0x01, 0x1a, 0x3d, 0x0a, 0x0f,
	0x41, 0x6c, 0x70, 0x68, 0x61, 0x52, 0x44, 0x61, 0x74, 0x61, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x12,
	0x10, 0x0a, 0x03, 0x6b, 0x65, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x6b, 0x65,
	0x79, 0x12, 0x14, 0x0a, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x01,
	0x52, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x3a, 0x02, 0x38, 0x01, 0x1a, 0x3b, 0x0a, 0x0d, 0x42,
	0x65, 0x74, 0x61, 0x44, 0x61, 0x74, 0x61, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x12, 0x10, 0x0a, 0x03,
	0x6b, 0x65, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x6b, 0x65, 0x79, 0x12, 0x14,
	0x0a, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x01, 0x52, 0x05, 0x76,
	0x61, 0x6c, 0x75, 0x65, 0x3a, 0x02, 0x38, 0x01, 0x1a, 0x3a, 0x0a, 0x0c, 0x52, 0x68, 0x6f, 0x44,
	0x61, 0x74, 0x61, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x12, 0x10, 0x0a, 0x03, 0x6b, 0x65, 0x79, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x6b, 0x65, 0x79, 0x12, 0x14, 0x0a, 0x05, 0x76, 0x61,
	0x6c, 0x75, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x01, 0x52, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65,
	0x3a, 0x02, 0x38, 0x01, 0x22, 0x58, 0x0a, 0x08, 0x53, 0x70, 0x6f, 0x74, 0x44, 0x61, 0x74, 0x61,
	0x12, 0x12, 0x0a, 0x04, 0x6f, 0x70, 0x65, 0x6e, 0x18, 0x01, 0x20, 0x01, 0x28, 0x01, 0x52, 0x04,
	0x6f, 0x70, 0x65, 0x6e, 0x12, 0x10, 0x0a, 0x03, 0x6c, 0x6f, 0x77, 0x18, 0x02, 0x20, 0x01, 0x28,
	0x01, 0x52, 0x03, 0x6c, 0x6f, 0x77, 0x12, 0x12, 0x0a, 0x04, 0x68, 0x69, 0x67, 0x68, 0x18, 0x03,
	0x20, 0x01, 0x28, 0x01, 0x52, 0x04, 0x68, 0x69, 0x67, 0x68, 0x12, 0x12, 0x0a, 0x04, 0x73, 0x70,
	0x6f, 0x74, 0x18, 0x04, 0x20, 0x01, 0x28, 0x01, 0x52, 0x04, 0x73, 0x70, 0x6f, 0x74, 0x2a, 0x37,
	0x0a, 0x0a, 0x54, 0x61, 0x72, 0x67, 0x65, 0x74, 0x44, 0x61, 0x74, 0x61, 0x12, 0x16, 0x0a, 0x12,
	0x54, 0x41, 0x52, 0x47, 0x45, 0x54, 0x44, 0x41, 0x54, 0x41, 0x5f, 0x55, 0x4e, 0x4b, 0x4e, 0x4f,
	0x57, 0x4e, 0x10, 0x00, 0x12, 0x08, 0x0a, 0x04, 0x53, 0x50, 0x4f, 0x54, 0x10, 0x01, 0x12, 0x07,
	0x0a, 0x03, 0x56, 0x4f, 0x4c, 0x10, 0x02, 0x32, 0x63, 0x0a, 0x13, 0x52, 0x65, 0x61, 0x6c, 0x74,
	0x69, 0x6d, 0x65, 0x44, 0x61, 0x74, 0x61, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0x4c,
	0x0a, 0x17, 0x53, 0x74, 0x61, 0x72, 0x74, 0x52, 0x65, 0x61, 0x6c, 0x74, 0x69, 0x6d, 0x65, 0x4d,
	0x61, 0x72, 0x6b, 0x65, 0x74, 0x46, 0x65, 0x65, 0x64, 0x12, 0x16, 0x2e, 0x52, 0x65, 0x61, 0x6c,
	0x74, 0x69, 0x6d, 0x65, 0x4d, 0x61, 0x72, 0x6b, 0x65, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73,
	0x74, 0x1a, 0x17, 0x2e, 0x52, 0x65, 0x61, 0x6c, 0x74, 0x69, 0x6d, 0x65, 0x4d, 0x61, 0x72, 0x6b,
	0x65, 0x74, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x30, 0x01, 0x42, 0x1e, 0x5a, 0x04,
	0x2e, 0x2f, 0x70, 0x62, 0xaa, 0x02, 0x15, 0x52, 0x65, 0x61, 0x6c, 0x74, 0x69, 0x6d, 0x65, 0x4d,
	0x61, 0x72, 0x6b, 0x65, 0x74, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x62, 0x06, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_realtime_update_proto_rawDescOnce sync.Once
	file_realtime_update_proto_rawDescData = file_realtime_update_proto_rawDesc
)

func file_realtime_update_proto_rawDescGZIP() []byte {
	file_realtime_update_proto_rawDescOnce.Do(func() {
		file_realtime_update_proto_rawDescData = protoimpl.X.CompressGZIP(file_realtime_update_proto_rawDescData)
	})
	return file_realtime_update_proto_rawDescData
}

var file_realtime_update_proto_enumTypes = make([]protoimpl.EnumInfo, 1)
var file_realtime_update_proto_msgTypes = make([]protoimpl.MessageInfo, 9)
var file_realtime_update_proto_goTypes = []any{
	(TargetData)(0),                // 0: TargetData
	(*RealtimeMarketRequest)(nil),  // 1: RealtimeMarketRequest
	(*RealtimeMarketResponse)(nil), // 2: RealtimeMarketResponse
	(*EquityData)(nil),             // 3: EquityData
	(*SpotData)(nil),               // 4: SpotData
	nil,                            // 5: EquityData.SigmaDataEntry
	nil,                            // 6: EquityData.AlphaDataEntry
	nil,                            // 7: EquityData.AlphaRDataEntry
	nil,                            // 8: EquityData.BetaDataEntry
	nil,                            // 9: EquityData.RhoDataEntry
}
var file_realtime_update_proto_depIdxs = []int32{
	0, // 0: RealtimeMarketRequest.target_data_list:type_name -> TargetData
	3, // 1: RealtimeMarketResponse.equity_data_list:type_name -> EquityData
	4, // 2: EquityData.spot_data:type_name -> SpotData
	5, // 3: EquityData.sigma_data:type_name -> EquityData.SigmaDataEntry
	6, // 4: EquityData.alpha_data:type_name -> EquityData.AlphaDataEntry
	7, // 5: EquityData.alphaR_data:type_name -> EquityData.AlphaRDataEntry
	8, // 6: EquityData.beta_data:type_name -> EquityData.BetaDataEntry
	9, // 7: EquityData.rho_data:type_name -> EquityData.RhoDataEntry
	1, // 8: RealtimeDataService.StartRealtimeMarketFeed:input_type -> RealtimeMarketRequest
	2, // 9: RealtimeDataService.StartRealtimeMarketFeed:output_type -> RealtimeMarketResponse
	9, // [9:10] is the sub-list for method output_type
	8, // [8:9] is the sub-list for method input_type
	8, // [8:8] is the sub-list for extension type_name
	8, // [8:8] is the sub-list for extension extendee
	0, // [0:8] is the sub-list for field type_name
}

func init() { file_realtime_update_proto_init() }
func file_realtime_update_proto_init() {
	if File_realtime_update_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_realtime_update_proto_msgTypes[0].Exporter = func(v any, i int) any {
			switch v := v.(*RealtimeMarketRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_realtime_update_proto_msgTypes[1].Exporter = func(v any, i int) any {
			switch v := v.(*RealtimeMarketResponse); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_realtime_update_proto_msgTypes[2].Exporter = func(v any, i int) any {
			switch v := v.(*EquityData); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_realtime_update_proto_msgTypes[3].Exporter = func(v any, i int) any {
			switch v := v.(*SpotData); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_realtime_update_proto_rawDesc,
			NumEnums:      1,
			NumMessages:   9,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_realtime_update_proto_goTypes,
		DependencyIndexes: file_realtime_update_proto_depIdxs,
		EnumInfos:         file_realtime_update_proto_enumTypes,
		MessageInfos:      file_realtime_update_proto_msgTypes,
	}.Build()
	File_realtime_update_proto = out.File
	file_realtime_update_proto_rawDesc = nil
	file_realtime_update_proto_goTypes = nil
	file_realtime_update_proto_depIdxs = nil
}
