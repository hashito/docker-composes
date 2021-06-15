FROM ubuntu
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt update && apt -y install git && apt -y install tzdata
RUN mkdir -p /usr/bin/composer
COPY --from=composer:1.10.13 /usr/bin/composer /usr/bin/composer
