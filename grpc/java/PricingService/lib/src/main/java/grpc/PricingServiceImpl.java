package grpc;

import grpc.PricingServiceGrpc;
import grpc.PricingServiceOuterClass.PricingRequest;
import grpc.PricingServiceOuterClass.PricingResponse;
import io.grpc.stub.StreamObserver;

public class PricingServiceImpl extends PricingServiceGrpc.PricingServiceImplBase {
	@Override
	public void pricing(PricingRequest request, StreamObserver<PricingResponse> responseObserver) {
		PricingResponse response = PricingResponse.newBuilder()
				.setResponse("Hello" + request.getRequest())
				.build();
		responseObserver.onNext(response);
		responseObserver.onCompleted();
	}
}
