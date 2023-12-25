import { Test, TestingModule } from '@nestjs/testing';
import { LedService } from './led.service';

describe('LedService', () => {
  let service: LedService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [LedService],
    }).compile();

    service = module.get<LedService>(LedService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});
