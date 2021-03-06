FROM golang:latest
RUN mkdir /go/src/work
WORKDIR /go/src/work
ADD . /go/src/work

RUN go get github.com/gin-gonic/gin
RUN go get github.com/go-sql-driver/mysql
RUN go get github.com/jinzhu/gorm