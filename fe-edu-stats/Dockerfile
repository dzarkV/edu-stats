FROM node:lts-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install @vue/cli -g

COPY packag*.json .
COPY src .
RUN npm install
EXPOSE 4173
CMD ["npm", "run", "preview"]
