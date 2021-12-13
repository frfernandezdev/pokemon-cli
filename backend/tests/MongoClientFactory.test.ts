import { MongoClientFactory } from 'src/modules/core/infrastructure/persistence/MongoClientFactory';
import { MongoClient } from 'mongodb';

describe('ConnectionMongo', () => {
  describe('#createClient', () => {
    const factory = MongoClientFactory;
    let client: MongoClient;

    beforeEach(async () => {
      client = await factory.createClient('test', { url: 'mongodb://localhost:27017/test-backend' });
    });

    afterEach(async () => {
      await client.close();
    });

    it('creates a new client with the connection already established', async () => {
      expect(client).toBeInstanceOf(MongoClient);
      const ping = await client.db('admin').command({ ping: 1 });
      expect(ping).toMatchObject({ ok: 1 });
    });

    it('create a new client if it does not exist a client with the given name', async () => {
      const newClient = await factory.createClient('test2', { url: 'mongodb://localhost:27017/test-backend' });
      expect(newClient).not.toBe(client);

      await newClient.close();
    });

    it('returns a client if it already exists', async () => {
      const newClient = await factory.createClient('test', { url: 'mongodb://localhost:27017/test-backend' });

      expect(newClient).toBe(client);

      await newClient.close();
    });
  });
});
