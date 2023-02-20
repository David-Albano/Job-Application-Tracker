
let dataTable;
let dataTableIsInitialized=false;

const dataTableOptions = {
    columnDefs:[
        { className: "centered", targets: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]},
        { className: "width_cells", targets: [1, 2, 3, 4, 5, 6, 7, 8, 10]},
        { className: "platform", targets: [4]},
        { orderable: false, targets:[3, 4, 7, 8, 9, 10] },
        { searchable: false, targets:[0, 8, 10] }
    ],
    destroy: true
};

const initDataTable=async()=>{
    if(dataTableIsInitialized){
        dataTable.destroy();
    };

    await listApplications();

    dataTable = $('#db-applications').DataTable(dataTableOptions);

    dataTableIsInitialized=true;
};

const listApplications=async()=>{
    try{
        const response=await fetch('http://127.0.0.1:8000/tracker/applications');
        const data = await response.json();

        let content = ``;
        data.applications.forEach((applications, index)=>{
            content +=  `
                <tr>
                    <td>${index+1}</td>
                    <td>
                        <div class="bg-info rounded">${applications.company}</div>
                    </td>
                    <td><div class="bg-success rounded">${applications.role}</div></td>
                    <td><div class="rounded" style='background: #fd7e14;'>${applications.stage}</div></td>
                    <td><div class="bg-primary rounded platform">${applications.platform}</div></td>
                    <td><div>${applications.app_date}</div></td>
                    <td><div>${applications.last_contact}</div></td>
                    <td>
                        <a href="show_job_info/${applications.id}">
                            <button class="btn btn-info" title="Job Desciption Info">
                                <i class="fa-solid fa-circle-info"></i>
                            </button>
                        </a>
                    </td>
                    <td>
                        <a href="show_comment/${applications.id}">
                            <button class="btn btn-warning" title="Comment">
                                <i class="fa-solid fa-comment-dots"></i>
                            </button>
                        </a>
                    </td>
                    <td><div class="bg-primary rounded">${applications.contact}</div></td>
                    <td>
                        <div class='d-flex-between'>
                            <a href="edit_application/${applications.id}">
                                <button class="btn btn-primary" title="Edit application"><i class="fa-solid fa-pencil"></i></button>
                            </a>
                            <a href="delete_application/${applications.id}">
                                <button class="btn btn-danger" title="Delete application"><i class="fa-solid fa-trash-can"></i></button>
                            </a>
                        </div>
                    </td>
                </tr>
            `
        });
        tableBody_applications.innerHTML = content;
    } catch (ex) {
        console.error(ex);
        alert(ex);
    }
};

window.addEventListener('load', async ()=> {
    await initDataTable();
});