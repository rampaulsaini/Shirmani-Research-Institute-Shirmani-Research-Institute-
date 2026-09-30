FROM node:22-alpine

WORKDIR /app
ENV NODE_ENV=production
ENV PORT=8787

COPY package.json ./
RUN npm install --omit=dev && npm cache clean --force

COPY src ./src
COPY sql ./sql
COPY README.md ./

EXPOSE 8787

USER node

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD node -e "fetch('http://127.0.0.1:' + (process.env.PORT || 8787) + '/v1/platform/readiness').then(r=>process.exit(r.ok?0:1)).catch(()=>process.exit(1))"

CMD ["node","src/index.js"]
