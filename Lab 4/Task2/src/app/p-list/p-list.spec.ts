import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PList } from './p-list';

describe('PList', () => {
  let component: PList;
  let fixture: ComponentFixture<PList>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PList]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PList);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
