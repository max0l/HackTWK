FROM node:22-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run compile

EXPOSE 3000

CMD ["node", "src/index.js"]
