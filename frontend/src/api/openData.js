import axios from 'axios'

export const getData = function(){
    return axios({url: "/getRapidTestKits", method: "get"})
}