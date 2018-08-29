

class DataService {

    gender = '';

    set gender(value) {
        this.gender = value;
    }

}

class DataServiceSingleton {

    getInstace() {
        if(this.dataService == undefined || this.dataService == null)
            this.dataService = new DataService
        return this.dataService;
    }
    
    
}

export default DataServiceSingleton;