// thanks https://github.com/prisma/prisma/discussions/10037#discussioncomment-1569084

import { PrismaClient } from "@prisma/client";

let prisma: PrismaClient;
prisma = new PrismaClient();

/*if (process.env.NODE_ENV === "production") {
  prisma = new PrismaClient();
} else {
  let globalWithPrisma = global as typeof globalThis & {
    prisma: PrismaClient;
  };
  if (!globalWithPrisma.prisma) {
    globalWithPrisma.prisma = new PrismaClient();
  }
  prisma = globalWithPrisma.prisma;
}*/

export default prisma;
