const serverUrl = "";
const appId = "";
Moralis.start({ serverUrl, appId });
const getInfo = async () => {
  const options = {
    network: document.getElementById("network").value,
    address: document.getElementById("address").value,};
  const portfolio = await Moralis.SolanaAPI.account.getPortfolio(options);
  console.log(portfolio);};
document.getElementById("get-NFTs").onclick = getInfo();