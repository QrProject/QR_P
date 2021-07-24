import styles from '@/styles/Table.module.scss';
import React from 'react';

interface Props {
  list: any;
}

export const BasicTable: React.FC<Props> = ({ list }) => {

  return (
    <div className={styles.table}>
      { list.map((v:any, i:number) => {
        return (
          <div className={styles.row} key={`${v}-${i}`}>
            <div className={styles.row__left}>{v.title}</div>
            <div className={styles.row__right}>{v.value}</div>
          </div>
        );
      })}
    </div>
  )
}