# Python Examples

Included are three basic examples for working with the MAPP API:
- Upload - loads a new file into MAPP and recieves your FileID for the job.
- Status - tells you the status of a particular job.
- Jobs - lists back any open or closed jobs you have submitted via the API.

## Security / Passwords / Tokens

Storing passwords, credentials, and tokens directly in code is never advisable. 
There are many methods for storing these outside of your code and then using a 
helper function to retrieve them at runtime. Four great options of varying complexity:

1. Store them in a config file that you exclude from your repository.
2. Store them as environment variables for your user.
3. Store them in a NoSQL database like MongoDB or DynamoDB for lookup.
4. Use a discovery service like CONSUL (consul.io) that can provide a datacenter-wide key-value store for retrieval.
