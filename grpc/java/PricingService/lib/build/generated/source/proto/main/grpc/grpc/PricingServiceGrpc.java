package grpc;

import static io.grpc.MethodDescriptor.generateFullMethodName;
import static io.grpc.stub.ClientCalls.asyncBidiStreamingCall;
import static io.grpc.stub.ClientCalls.asyncClientStreamingCall;
import static io.grpc.stub.ClientCalls.asyncServerStreamingCall;
import static io.grpc.stub.ClientCalls.asyncUnaryCall;
import static io.grpc.stub.ClientCalls.blockingServerStreamingCall;
import static io.grpc.stub.ClientCalls.blockingUnaryCall;
import static io.grpc.stub.ClientCalls.futureUnaryCall;
import static io.grpc.stub.ServerCalls.asyncBidiStreamingCall;
import static io.grpc.stub.ServerCalls.asyncClientStreamingCall;
import static io.grpc.stub.ServerCalls.asyncServerStreamingCall;
import static io.grpc.stub.ServerCalls.asyncUnaryCall;
import static io.grpc.stub.ServerCalls.asyncUnimplementedStreamingCall;
import static io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall;

/**
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.23.0)",
    comments = "Source: PricingService.proto")
public final class PricingServiceGrpc {

  private PricingServiceGrpc() {}

  public static final String SERVICE_NAME = "grpc.PricingService";

  // Static method descriptors that strictly reflect the proto.
  private static volatile io.grpc.MethodDescriptor<grpc.PricingServiceOuterClass.PricingRequest,
      grpc.PricingServiceOuterClass.PricingResponse> getPricingMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "Pricing",
      requestType = grpc.PricingServiceOuterClass.PricingRequest.class,
      responseType = grpc.PricingServiceOuterClass.PricingResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<grpc.PricingServiceOuterClass.PricingRequest,
      grpc.PricingServiceOuterClass.PricingResponse> getPricingMethod() {
    io.grpc.MethodDescriptor<grpc.PricingServiceOuterClass.PricingRequest, grpc.PricingServiceOuterClass.PricingResponse> getPricingMethod;
    if ((getPricingMethod = PricingServiceGrpc.getPricingMethod) == null) {
      synchronized (PricingServiceGrpc.class) {
        if ((getPricingMethod = PricingServiceGrpc.getPricingMethod) == null) {
          PricingServiceGrpc.getPricingMethod = getPricingMethod =
              io.grpc.MethodDescriptor.<grpc.PricingServiceOuterClass.PricingRequest, grpc.PricingServiceOuterClass.PricingResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "Pricing"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  grpc.PricingServiceOuterClass.PricingRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  grpc.PricingServiceOuterClass.PricingResponse.getDefaultInstance()))
              .setSchemaDescriptor(new PricingServiceMethodDescriptorSupplier("Pricing"))
              .build();
        }
      }
    }
    return getPricingMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static PricingServiceStub newStub(io.grpc.Channel channel) {
    return new PricingServiceStub(channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static PricingServiceBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    return new PricingServiceBlockingStub(channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static PricingServiceFutureStub newFutureStub(
      io.grpc.Channel channel) {
    return new PricingServiceFutureStub(channel);
  }

  /**
   */
  public static abstract class PricingServiceImplBase implements io.grpc.BindableService {

    /**
     */
    public void pricing(grpc.PricingServiceOuterClass.PricingRequest request,
        io.grpc.stub.StreamObserver<grpc.PricingServiceOuterClass.PricingResponse> responseObserver) {
      asyncUnimplementedUnaryCall(getPricingMethod(), responseObserver);
    }

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
          .addMethod(
            getPricingMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                grpc.PricingServiceOuterClass.PricingRequest,
                grpc.PricingServiceOuterClass.PricingResponse>(
                  this, METHODID_PRICING)))
          .build();
    }
  }

  /**
   */
  public static final class PricingServiceStub extends io.grpc.stub.AbstractStub<PricingServiceStub> {
    private PricingServiceStub(io.grpc.Channel channel) {
      super(channel);
    }

    private PricingServiceStub(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected PricingServiceStub build(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      return new PricingServiceStub(channel, callOptions);
    }

    /**
     */
    public void pricing(grpc.PricingServiceOuterClass.PricingRequest request,
        io.grpc.stub.StreamObserver<grpc.PricingServiceOuterClass.PricingResponse> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getPricingMethod(), getCallOptions()), request, responseObserver);
    }
  }

  /**
   */
  public static final class PricingServiceBlockingStub extends io.grpc.stub.AbstractStub<PricingServiceBlockingStub> {
    private PricingServiceBlockingStub(io.grpc.Channel channel) {
      super(channel);
    }

    private PricingServiceBlockingStub(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected PricingServiceBlockingStub build(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      return new PricingServiceBlockingStub(channel, callOptions);
    }

    /**
     */
    public grpc.PricingServiceOuterClass.PricingResponse pricing(grpc.PricingServiceOuterClass.PricingRequest request) {
      return blockingUnaryCall(
          getChannel(), getPricingMethod(), getCallOptions(), request);
    }
  }

  /**
   */
  public static final class PricingServiceFutureStub extends io.grpc.stub.AbstractStub<PricingServiceFutureStub> {
    private PricingServiceFutureStub(io.grpc.Channel channel) {
      super(channel);
    }

    private PricingServiceFutureStub(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected PricingServiceFutureStub build(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      return new PricingServiceFutureStub(channel, callOptions);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<grpc.PricingServiceOuterClass.PricingResponse> pricing(
        grpc.PricingServiceOuterClass.PricingRequest request) {
      return futureUnaryCall(
          getChannel().newCall(getPricingMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_PRICING = 0;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final PricingServiceImplBase serviceImpl;
    private final int methodId;

    MethodHandlers(PricingServiceImplBase serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_PRICING:
          serviceImpl.pricing((grpc.PricingServiceOuterClass.PricingRequest) request,
              (io.grpc.stub.StreamObserver<grpc.PricingServiceOuterClass.PricingResponse>) responseObserver);
          break;
        default:
          throw new AssertionError();
      }
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public io.grpc.stub.StreamObserver<Req> invoke(
        io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        default:
          throw new AssertionError();
      }
    }
  }

  private static abstract class PricingServiceBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    PricingServiceBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return grpc.PricingServiceOuterClass.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("PricingService");
    }
  }

  private static final class PricingServiceFileDescriptorSupplier
      extends PricingServiceBaseDescriptorSupplier {
    PricingServiceFileDescriptorSupplier() {}
  }

  private static final class PricingServiceMethodDescriptorSupplier
      extends PricingServiceBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final String methodName;

    PricingServiceMethodDescriptorSupplier(String methodName) {
      this.methodName = methodName;
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.MethodDescriptor getMethodDescriptor() {
      return getServiceDescriptor().findMethodByName(methodName);
    }
  }

  private static volatile io.grpc.ServiceDescriptor serviceDescriptor;

  public static io.grpc.ServiceDescriptor getServiceDescriptor() {
    io.grpc.ServiceDescriptor result = serviceDescriptor;
    if (result == null) {
      synchronized (PricingServiceGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new PricingServiceFileDescriptorSupplier())
              .addMethod(getPricingMethod())
              .build();
        }
      }
    }
    return result;
  }
}
