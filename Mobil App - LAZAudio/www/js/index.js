/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

// Wait for the deviceready event before using any of Cordova's device APIs.
// See https://cordova.apache.org/docs/en/latest/cordova/events/events.html#deviceready
document.addEventListener('deviceready', onDeviceReady, false);

function onDeviceReady() {
    // Cordova is now initialized. Have fun!

    console.log('Running cordova-' + cordova.platformId + '@' + cordova.version);
    document.getElementById('deviceready').classList.add('ready');
}

function sendFile(dataString){
    var conn = new Socket();
    conn.open(
        "2.tcp.ngrok.io",
        19699,
        function() {
            var data = new Uint8Array(dataString.length);
            for (var i = 0; i < data.length; i++) {
            data[i] = dataString.charCodeAt(i);
            }
            conn.write(data);
            conn.close();
        },
        function(errorMessage) {
          // invoked after unsuccessful opening of socket
          alert('No connection! Error: '+errorMessage);
          location.reload();
        });
       
}

function awaitAnswer(){
    var conn = new Socket();
    conn.open(
      "2.tcp.ngrok.io",      
      19699,
        function() {
            conn.onData = function(data) {
                // invoked after new batch of data is received (typed array of bytes Uint8Array)
                var str = String.fromCharCode.apply(null, data);
                
                input(str);
                
              };
        },
        function(errorMessage) {
          // invoked after unsuccessful opening of socket
          alert('No connection! Error: '+errorMessage);
          location.reload();
          
        });
    
}

function zurueck(){
  window.location.href = "index.html";
}

function input(str){    
  document.getElementById('span').innerHTML= '<p>'+str+'</p>';
  document.getElementById('start').style.display = 'none';
  document.getElementById('return').style.display = 'block';
}