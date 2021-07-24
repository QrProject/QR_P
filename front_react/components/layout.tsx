import React, { FC } from "react";
import Headers from './headers';
import styles from '@/styles/Layout.module.scss';


export default function Layout(prop: any) {
  return (
    <div className={styles.layout}>
      <Headers />
      <main>{prop.children}</main>
    </div>
  )
}