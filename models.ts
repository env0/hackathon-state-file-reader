import * as pydantic from 'pydantic';

enum SupportedTFVersions {
    V0_12 = '0.12',
    V0_13 = '0.13',
    V0_14 = '0.14',
    V1_0 = '1.0',
}

class ResourceMode extends String {
    static managed = 'managed';
    static data = 'data';
}

class Resource extends pydantic.BaseModel {
    mode: ResourceMode;
    type: string;
    name: string;
    provider: string;
    instances?: Record<string, unknown>[];

    constructor(data: {
        mode: ResourceMode;
        type: string;
        name: string;
        provider: string;
        instances?: Record<string, unknown>[];
    }) {
        super();
        Object.assign(this, data);
    }
}

class TerraformState extends pydantic.BaseModel {
    version: number;
    terraform_version: string;
    serial: number;
    lineage: string;
    outputs: Record<string, unknown>;
    resources: Resource[];

    constructor(data: {
        version: number;
        terraform_version: string;
        serial: number;
        lineage: string;
        outputs: Record<string, unknown>;
        resources: Resource[];
    }) {
        super();
        Object.assign(this, data);
    }
}