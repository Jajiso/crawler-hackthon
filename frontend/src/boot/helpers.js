import { boot } from 'quasar/wrappers'
import companiesObj1 from '../../../Crawler/FrontEnd_Companies.json';


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
export default boot(({ app }) => {
  app.config.globalProperties.$companies1 = formatCompanyJson(companiesObj1)
})

export { formatCompanyJson }
