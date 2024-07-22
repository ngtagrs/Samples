export default class Issue {
    id: number = 0;
    title: string = "";
    description: string = "";
    category: string = "";
    status: string = "未着手";
    representative: string = ""
    last_updated_at: Date = new Date();
    created_at: Date = new Date();

    work_logs: WorkLog[] = []
    comments: IssueComment[] = []
    files: File[] = []

    constructor(title: string, description: string){
        this.title = title;
        this.description = description;
    }
}
class WorkLog {
    title: string = "";
    description: string="";
    files: File[] = []
    worked_by: string = "";
    worked_at: Date = new Date();
}
class IssueComment {
    comment: string="";
    files: File[] = []
    commented_by: string = "";
    commented_at: Date = new Date();
}