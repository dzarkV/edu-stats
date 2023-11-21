FROM node:18-alpine as build-stage

WORKDIR /app
COPY packag*.json .
COPY index.html .
COPY src /app/src
RUN npm install
RUN npm run build

FROM danjellz/http-server:1.4 as production-stage
COPY --from=build-stage /app/dist /public
CMD ["http-server", "-p", "9000"]