FROM node:14.11.0 as builder
RUN apt-get update && apt-get install git
RUN cd /root/ && \
    git clone https://github.com/sitepoint-editors/angular-todo-app.git && \
    cd angular-todo-app && \
    npm install && \
    echo "export const environment = {production: true,apiUrl: 'http://localhost'};">src/environments/environment.ts && \
    npm run build

FROM nginx:1.19.2
RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /root/angular-todo-app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]