import { boot } from 'quasar/wrappers'
import companiesObj1 from '../../../Crawler/FrontEnd_Companies.json';
import companiesObj2 from '../../../Crawler/Reed_Companies.json';


const formatCompanyJson = (bussinessObj) => {
    const result = []
    for (const [key, value] of Object.entries(bussinessObj["Company Name"])) {
        const obj = {
            title: value,
            location: bussinessObj["Location"][key],
            website: bussinessObj["Website:"][key],
            logo: bussinessObj["Logo"][key]
        }
        result.push(obj)
    }
    return result
}

const formatCompanyJson2 = (bussinessObj) => {
    const result = []
    for (const [key, value] of Object.entries(bussinessObj["Company Name"])) {
        const obj = {
            title: value,
            // location: bussinessObj["Location"][key],
            size: bussinessObj["Size"][key],
            // sector: bussinessObj["Sector"][key]
        }
        result.push(obj)
    }
    return result
}

const filterDuplicates = (listObj) => {

    const result = listObj
    console.log(result);
    const filteredArr = result.reduce((acc, current) => {
    const x = acc.find(item => item.title === current.title);
        if (!x) {
            return acc.concat([current]);
        } else {
            return acc;
        }
    }, []);

    return filteredArr
}

export default boot(({ app }) => {
  app.config.globalProperties.$companies1 = formatCompanyJson(companiesObj1)
  app.config.globalProperties.$companies2 = formatCompanyJson2(companiesObj2)
  app.config.globalProperties.$filterDuplicates = filterDuplicates
})

