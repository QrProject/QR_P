import styles from '@/styles/pmp/Pmp.module.scss'
import Layout from 'components/layout';
import { BasicTable } from 'components/table/basic';
import Link from 'next/link';

const list = [
  { title: '현장명', value: '신나무실' },
  { title: '제조업체', value: '규석이네펌프(2005-7648)' },
  { title: '현장명', value: '신나무실' },
  { title: '제조일', value: '2021-01-01' },
  { title: '무상AS기간', value: '2021-01-01 - 2023-01-01' },
  { title: '유상수리업체', value: '규석이네펌프(2005-7648)' },
];

const list2 = [
  { title: '펌프모델명', value: 'DBS-G 10-3 2P 5HP' },
  { title: '펌프타입', value: '부스터펌프' },
  { title: '제조번호', value: 'ABC 00103' },
  { title: '구경', value: '100 * 100' },
  { title: '유량', value: '1 m3/min' },
  { title: '양정', value: '100M' },
];

const list3 = [
  { date: '2021-04-04', engineer: '오석기', content: '오히려 더 고장내고감' },
  { date: '2021-04-05', engineer: '양규석', content: '펌프에 대한 이해도 0' },
  { date: '2021-04-06', engineer: '최윤어', content: '안 옴' },
]

const videoId:number = 14;

export default function pmp() {
  return (
    <Layout>
      <section className={styles.container}>
        <div className="margin-b-20">
          <BasicTable list={list} />
        </div>
        <BasicTable list={list2} />
        <div className={styles['tools-wrap']}>
          <div className={styles.row}>
            <Link href={`/video/${videoId}`}>
              <div className={styles.tool}>사용 설명 동영상</div>
            </Link>
            <a className={styles.tool} href="/puppy.jpg" download target="_blank">시방서 다운로드</a>
          </div>
          <div className={styles.row}>
            <a className={styles.tool} href="/puppy.jpg" download target="_blank">도면 다운로드</a>
            <a className={styles.tool} href="/puppy.jpg" download target="_blank">성적서 다운로드</a>
          </div>
        </div>
        <div className={styles.table}>
          <div className={styles.title}>펌프수리내역</div>
            {
              list3.map(v => (
                <div className={styles['table-row']}>
                  <div className={styles.date}>{v.date}</div>
                  <div className={styles.engineer}>{v.engineer}</div>
                  <div className={styles.content}>{v.content}</div>
                </div>
              ))
            }
        </div>
      </section>
    </Layout>
  );
}