import { app } from "./app";

const port = process.env.PORT || 3000;

app.listen(port, () => {
  console.log(`NRM G&A API running on port ${port}.`);
});
