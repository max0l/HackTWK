FROM node:22-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN apk add --no-cache zip
RUN chmod +x /app/createZip.sh
RUN /app/createZip.sh

RUN npm run compile

EXPOSE 3000

CMD ["node", "src/index.js"]
