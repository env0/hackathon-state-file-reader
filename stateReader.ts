import * as fs from 'fs';

interface TerraformState {
    version: number;
    terraform_version: string;
    resources: Resource[];
}

interface Resource {
    name: string;
    mode: ResourceMode;
}

enum ResourceMode {
    managed = 'managed',
    other = 'other', // Add other resource modes as needed
}

class StateFileReader {
    private file_path: string;
    private data: TerraformState;

    constructor(file_path: string) {
        this.file_path = file_path;
        this.data = this.load_file();
    }

    private load_file(): TerraformState {
        try {
            const fileContent = fs.readFileSync(this.file_path, 'utf8');
            const data = JSON.parse(fileContent);
            return data as TerraformState;
        } catch (error) {
            console.error(`Error loading or validating state file: ${error}`);
            return {
                version: 0,
                terraform_version: '',
                resources: [],
            };
        }
    }

    list_resources(): string[] {
        return this.data.resources.map(resource => resource.name);
    }

    get_managed_resources(): Resource[] {
        return this.data.resources.filter(resource => resource.mode === ResourceMode.managed);
    }

    resource_exists(resource_name: string): boolean {
        return this.data.resources.some(resource => resource.name === resource_name);
    }

    get_resource_added_date(resource_name: string): string | null {
        for (const resource of this.data.resources) {
            if (resource.name === resource_name) {
                // TODO: Add functionality to get resource added date if possible
                return resource.model_dump(); // Replace with actual implementation
            }
        }
        return null;
    }
}