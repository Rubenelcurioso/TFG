FROM node:22 as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM node:22 as production-stage
WORKDIR /app
COPY --from=build-stage /app/.nuxt ./.nuxt
COPY --from=build-stage /app/package*.json ./
EXPOSE 3000
CMD ["node", "start"]