import "reflect-metadata";
import * as tq from "type-graphql";
import { UserResolver } from "../../server/graphql/UserResolver";
import { ApolloServer } from "apollo-server";
import { DateTimeResolver } from "graphql-scalars";
import { context } from "../../../../server/graphql/context";
import { GraphQLScalarType } from "graphql";

const app = async () => {
  const schema = await tq.buildSchema({
    resolvers: [PostResolver, UserResolver, PostCreateInput],
    scalarsMap: [{ type: GraphQLScalarType, scalar: DateTimeResolver }],
  });

  new ApolloServer({ schema, context: context }).listen({ port: 4000 }, () =>
    console.log(`
🚀 Server ready at: http://localhost:4000
⭐️  See sample queries: http://pris.ly/e/ts/graphql-typegraphql#using-the-graphql-api`)
  );
};

app();
