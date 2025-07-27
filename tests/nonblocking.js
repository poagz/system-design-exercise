import http from "k6/http";
import { check } from "k6";
import { SharedArray } from "k6/data";

const users = new SharedArray("users", function () {
  const text = open("./data.csv");
  const lines = text.split("\n").slice(1);
  return lines.map(line => line.trim()).filter(line => line !== "");
});

export let options = {
  vus: 10,
  duration: "5s",
};

export default function () {
  users.forEach(name => {
    let payload = JSON.stringify({ name: name });
    let res = http.post("http://localhost:8001/users", payload, {
      headers: { "Content-Type": "application/json" },
    });

    check(res, { "status is 200": (r) => r.status === 200 });
  });
}

