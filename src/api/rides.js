import { mockRides } from "../mocks/rides";

// TODO: 後端做好列表 API 後，改成 api.get("/路徑") 並 return res.data
export async function getRides() {
  return mockRides;
}

export async function createRide(ride) {
  // TODO: 後端做好後改成 api.post("/路徑", ride)，並 return res.data
  console.log("發起共乘：", ride);
  return true;
}