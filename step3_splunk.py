from pathlib import Path

Path("backend/server.js").write_text("""
const express = require("express");
const cors = require("cors");
const axios = require("axios");
require("dotenv").config();

const https = require("https");

const app = express();

app.use(cors());
app.use(express.json());

app.get("/", (req,res)=>{
    res.send("OncoConnect Backend Running");
});

app.post("/test-splunk", async (req,res)=>{

    try{

        const payload = {
            sourcetype:"oncoconnect:test",
            index:process.env.SPLUNK_INDEX,
            event:{
                app:"OncoConnect AI",
                message:"First event from OncoConnect",
                timestamp:new Date().toISOString()
            }
        };

        const response = await axios.post(
            process.env.SPLUNK_HEC_URL,
            payload,
            {
                headers:{
                    Authorization:`Splunk ${process.env.SPLUNK_HEC_TOKEN}`
                },
                httpsAgent:new https.Agent({
                    rejectUnauthorized:false
                })
            }
        );

        res.json({
            success:true,
            splunk:response.data
        });

    }catch(error){

        console.log(error.response?.data || error.message);

        res.status(500).json({
            success:false,
            error:error.message
        });

    }

});

app.listen(5050,()=>{
    console.log("Server running on port 5050");
});
""", encoding="utf-8")

print("server.js updated")
