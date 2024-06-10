FROM rust:1.77-slim-buster

COPY application/ application/

RUN cd application && cargo build --release

ENTRYPOINT [ "./application/target/release/application"]
